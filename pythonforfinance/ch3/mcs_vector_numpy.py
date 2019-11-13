#
# NumPy로 구현한 유러피안 콜 옵션의 몬테카를로 가격 계산
# mcs_vector_numpy.py
#


import math
import numpy as np
from time import time

np.random.seed(2000)
t0 = time()

# 파라미터
S0 = 100.; K = 105.; T = 1.0; r = 0.05; sigma = 0.2
M = 50; dt = T / M; I = 250000

# 경로 하나당 M개의 시간 구현을 가지는 I개의 샘플 경로를 생성
S = np.zeros((M + 1, I))
S[0] = S0
for t in range(1, M + 1):
    z = np.random.standard_normal(I) # pseudorandom numbers
    S[t] = S[t-1] * np.exp((r - 0.5 * sigma ** 2) * dt
        + sigma * math.sqrt(dt) * z)
    # 모든 경로의 같은 시간 구간에 대해 벡터 연산 적용

# 몬테카를로 방법을 사용한 가격 추정
C0 = math.exp(-r * T) * np.sum(np.maximum(S[-1] - K, 0)) / I

# 결과 출력
tnp1 = time() - t0
print("European Option Value %7.3f" % C0)
print("Duration in Secods    %7.3f" % tnp1)