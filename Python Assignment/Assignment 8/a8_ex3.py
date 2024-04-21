import math

class StandardScaler:
    def __init__(self):
        self.mu=None
        self.sig=None

    def fit(self, features: list):
        
        if not all(isinstance(x, (int, float)) for x in features):
            raise ValueError("Features should contain only numerical values.")

        n = len(features)
        self.mu = sum(features) / n
        self.sig = math.sqrt(sum((x - self.mu) ** 2 for x in features) / (n - 1))

    def transform(self, features: list):
        
        if self.mu is None or self.sig is None:
            raise ValueError("Scaler has not been fitted.")

        return [(x - self.mu) / self.sig for x in features]

    def fit_transform(self, features: list):
        
        self.fit(features)
        return self.transform(features)

    def __getitem__(self, key):
        
        if not isinstance(key, int):
            raise TypeError("Indices must be integers")
        if key == 0:
            return self.mu
        elif key == 1:
            return self.sig
        else:
            raise IndexError("Index out of range")


# feats1 = [0,2,4,6,8,10]
# feats2 = [1,3,5,7,9]
# s = StandardScaler()
# print(s.mu, s.sig)
# s.fit(feats1)
# print(s[0], s[1])
# feats1_scaled = s.transform(feats1)
# print(feats1_scaled)
# feats2_scaled = s.transform(feats2)
# print(feats2_scaled)
# s = StandardScaler()
# feats2_scaled = s.fit_transform(feats2)
# print(feats2_scaled)
# print(s[0], s[1])
# s = StandardScaler()


# try:
#     s.transform(feats2)
# except ValueError as e:
#     print(f"{type(e).__name__}: {e}")
# try:
#     print(s["foo"])
# except TypeError as e:
#     print(f"{type(e).__name__}: {e}")
# try:
#     print(s[2])
# except IndexError as e:
#     print(f"{type(e).__name__}: {e}")