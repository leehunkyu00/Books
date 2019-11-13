# 파이썬만으로 구현한 유러피안 콜 옵션의 몬테카를로 가격 계산

from time import time
from math import exp, sqrt, log
from random import gauss, seed

seed(20000)
t0 = time()

# 인수
S0 = 100.   # 초깃값
K = 105.    # 행사가
T = 1.0     # 만기
r = 0.05    # 무위험 단기 이자율
sigma = 0.2 # 변동성
M = 50      # 시간 구간 개수
dt = T / M  # 하나의 시간 구간의 길이
I = 250000  # 샘플 경로의 수

# 경로 하나당 M 개의 시간 구간을 가지는 I개의 샘플 경로를 생성
S = []
for i in range(I):
    path = []
    for t in range(M + 1):
        if t == 0:
            path.append(S0)
        else:
            z = gauss(0.0, 1.0)
            St = path[t - 1] * exp((r - 0.5 * sigma ** 2) * dt + sigma * sqrt(dt) * z)
            path.append(St)
        S.append(path)

# 몬테카를로 방법을 사용한 가격 추정
C0 = exp(-r * T) * sum([max(path[-1] - K, 0) for path in S]) / I

# 결과 출력
tpy = time() - t0
print("European Option Value %7.3f" % C0)
print("Duration in Seconds   %7.3f" % tpy)