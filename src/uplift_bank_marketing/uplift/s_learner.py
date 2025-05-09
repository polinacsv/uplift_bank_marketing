# src/uplift_bank_marketing/uplift/s_learner.py

from sklearn.ensemble import GradientBoostingClassifier

def s_learner(X=None, treatment=None, outcome=None):
    """A basic implementation of an S-Learner for uplift modeling."""
    if X is None or treatment is None or outcome is None:
        print("S-Learner function works! (No data provided for training)")
        return None
    
    # Combining features and treatment
    X['treatment'] = treatment
    model = GradientBoostingClassifier()
    model.fit(X, outcome)
    print("S-Learner trained successfully.")
    return model
