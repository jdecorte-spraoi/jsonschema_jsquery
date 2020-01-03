from sct_jschema import __version__

from click.testing import CliRunner
from sct_jschema.cli import main
from sct_jschema.cli import get_type_for_key_path


def test_version():
    assert __version__ == "0.1.0"


def test_main():
    """ Test Main """
    runner = CliRunner()
    result = runner.invoke(main, [])
    assert result.exit_code == 2
    assert "Usage" in result.output


def test_main_help():
    """ Test Main """
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "Options" in result.output


def test_get_type_for_key_path_simple_path(test_schema):
    """ Test get_type_for_key_path with Simple Key Path """
    assert get_type_for_key_path(test_schema, "Age") == "integer"


def test_get_type_for_key_path_depth_one_level(test_schema):
    """ Test get_type_for_key_path with key path of one level deep """
    assert (
        get_type_for_key_path(test_schema, "EmploymentInformation.OriginalHireDate")
        == "string"
    )


def test_get_type_for_key_path_multi_level(test_schema):
    """ Test get_type_for_key_path with multi level key path """
    assert (
        get_type_for_key_path(test_schema, "EmploymentInformation.Beneficiary.Name")
        == "string"
    )


def test_get_type_for_key_path_invalid_key_path(test_schema):
    """ Test get_type_for_key_path with invalid key path """
    assert get_type_for_key_path(test_schema, "foo.bar") == None
