from session_6.sample import fatorial
import pytest

def test_fatorial_positivo():
    assert fatorial(5) == 120
    
    with pytest.raises(ValueError, match="O fatorial não é definido para números negativos"):
        fatorial(-1)