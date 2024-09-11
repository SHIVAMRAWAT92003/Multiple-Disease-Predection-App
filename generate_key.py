# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 16:01:05 2024

@author: SHIVAM RAWAT
"""


import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ["peter" ," parker"]
usernames = ["pt","pk"]
passwords = ["abc","def"]



hashed_passwords = stauth.Hasher(passwords).generate()


file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)
  














