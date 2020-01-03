import json

import click


def get_type_for_key_path(schema: dict, key_path: str) -> [str, None]:
    """
    Get the type for the given key path in the schema
    :param schema: JSON Schema in dictionary format
    :param key_path: Keys in a path separated by a period
    :return: Type associated with the element referenced by the key path or None

    """
    properties = schema.get("properties")
    keys = key_path.split(".")

    for key in keys:
        if key not in properties:
            return None
        if "type" in properties[key]:
            return properties[key]["type"]
        elif "$ref" in properties[key]:
            definition_key = properties[key]["$ref"].split("/")[-1]
            properties = schema.get("definitions").get(definition_key).get("properties")

    return None


@click.command()
@click.argument("schema_file", type=click.File("rb"))
@click.argument("key_path")
def main(schema_file: click.File, key_path: str):
    """ Given a valid JSON Schema and a valid key path, return the type value """
    schema_dict = json.load(schema_file)
    click.echo(f"Schema File = {schema_file.name}")
    click.echo(f"Key Path    = {key_path}")
    click.echo(
        f"Type        = {get_type_for_key_path(schema=schema_dict, key_path=key_path)}"
    )
