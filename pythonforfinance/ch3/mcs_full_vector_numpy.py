# Numpy로 구현한 유러피안 콜 옵션의 몬테카를로 가격 계산 (로그 버전)
# mcs_full_vector_numpy.py
#

import math
from numpy import *
from time import time

random.seed(2000)
t0 = time()

# 인수
S0 = 100.; K = 105.; T = 1.0; r = 0.05; sigma = 0.2
M = 50; dt = T / M; I = 250000

# 경로 하나당 M개의 시간 구간을 가지는 I개의 샘플 경로 생성
S = S0 * exp(cumsum((r - 0.5 * sigma ** 2) * dt
                    + sigma * math.sqrt(dt)
                            * random.standard_normal((M + 1, I)), axis = 0))

# 경로 전체가 아닌 마지막 값만 필요하다면 cumsum 대산 sum을 쓸 수도 있다.
S[0] = S0

# 몬테카를로 방법을 사용한 가격 추정
C0 = math.exp(-r * T) * sum(maximum(S[-1] - K, 0)) / I

# 결과 출력
tnp2 = time() - t0
print("European Option Value %7.3f" % C0)
print("Duration in Seconds   %7.3f" % tnp2)

