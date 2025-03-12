import pytest
from typer.testing import CliRunner
from session_8.main import app 

runner = CliRunner()

def test_square():
    result = runner.invoke(app, ["5", "--square"])
    assert result.exit_code == 0
    assert "resultado do quadrado: 25" in result.output

def test_addition():
    result = runner.invoke(app, ["5", "--valor2", "5", "--addition"])
    assert result.exit_code == 0
    assert "resultado da soma: 10" in result.output
