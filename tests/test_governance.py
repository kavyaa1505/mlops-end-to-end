import pytest
from feature_store.validation.feature_checks import detect_breaking_changes


def test_breaking_change_detection():
    current_features = {"feature_a"}
    registry_features = {"feature_a", "feature_b"}
    allowed = set()

    with pytest.raises(RuntimeError):
        detect_breaking_changes(
            current_features=current_features,
            registry_features=registry_features,
            allowed_breaks=allowed
        )
