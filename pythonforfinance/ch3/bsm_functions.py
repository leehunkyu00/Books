# 블랙-숄즈-머튼 모형을 사용한 유러피안 콜 옵션 가격결정
# 베가 계산 함수와 내재 변동성 추정 함수를 포함한다.
# file name : bsm_functions.py

def bsm_call_value(S0, K, T, r, sigma):
    """ 블랙-숄즈-머튼 모형을 사용한 유러피안 콜 옵션 가격결정 공식

    인수
    ===
    S0 : float
        초기 주가 혹은 지수
    K : float
        행사가
    T : float
        만기까지 남은 시간(연 단위)
    r : float
        고정 무위험 단기 이자율
    sigma : float
        변동성 파라미터

    반환값
    ===
    value : float
        유러피안 콜 옵션의 현재 가격
    """
    from math import log, sqrt, exp
    from scipy import stats

    S0 = float(S0)
    d1 = (log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    d2 = (log(S0 / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    value = (S0 * stats.norm.cdf(d1, 0.0, 1.0)
            - K * exp(-r * T) * stats.norm.cdf(d2, 0.0, 1.0))
            # stats.norm.cdf --> 정규분포의 누적확률 분포 계산
    return value

# 베가 계산 함수
def bsm_vega(S0, K, T, r, sigma):
    """ 블랙-숄즈-머튼 모형을 사용한 유러피안 옵션의 베가 계산

    인수
    ===
    S0 : float
        초기 주가 혹은 지수
    K : float
        행사가
    T : float
        만기까지 남은 시간(연 단위)
    r : float
        고정 무위험 단기 이자율
    sigma : float
        변동성 파라미터

    반환값
    ===
    vega : float
    블랙-숄즈-머튼 공식을 변동성에 대해 1차 미분한 값. 베가
    """
    from math import log, sqrt
    from scipy import stats

    S0 = float(S0)
    d1 = ((log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T)))
    vega = S0 * stats.norm.cdf(d1, 0.0, 1.0) * sqrt(T)

    return vega

# 내재 변동성 계산 함수
def bsm_call_imp_vol(S0, K, T, r, C0, sigma_est, it=100):
    """ 블랙-숄즈-머튼 모형을 사용한 유러피안 옵션의 내재 변동성 계산
    
    인수
    ===
    S0 : float
        초기 주가 혹은 지수
    K : float
        행사가
    T : float
        만기까지 남은 시간(연 단위)
    r : float
        고정 무위험 단기 이자율
    sigma_est :float
        변동성 파라미터 초기 추정치
    it : integer
        반복 계산 횟수

    반환값
    ===
    sigma_est : float
        수치적으로 추정한 내재 변동성
    """
    for i in range(it):
        sigma_est -= ((bsm_call_value(S0, K, T, r, sigma_est) - C0)
            / bsm_vega(S0, K, T, r, sigma_est))

    return sigma_est



