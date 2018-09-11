import json
from .api import api


def preprocess_tad(data):
    data['발생년'] = data['year']          # 발생년
    del data['year']

    data['발생월일'] = data['dt_006']       # 발생월일
    del data['dt_006']

    data['발생시간'] = data['dt_006_lv8']      # 발생시간
    del data['dt_006_lv8']

    data['주야구분코드'] = data['cd_008']          # 주야구분코드
    del data['cd_008']

    data['사고요일코드'] = data['cd_007']          # 사고요일코드
    del data['cd_007']

    data['사망자수'] = data['no_010']          # 사망자수
    del data['no_010']

    data['부상자수'] = data['injpsn_co']       # 부상자수
    del data['injpsn_co']

    data['중상자수'] = data['no_011']          # 중상자수
    del data['no_011']

    data['경상자수'] = data['no_012']          # 경상자수
    del data['no_012']

    data['부상신고자수'] = data['no_013']          # 부상신고자수
    del data['no_013']

    data['방생지시코드'] = data['cd_003_lv1']      # 발생지시코드
    del data['cd_003_lv1']

    data['발생지시군구코드'] = data['cd_003']          # 발생지시군구코드
    del data['cd_003']

    data['사고유형대분류코드'] = data['cd_014_lv1']      # 사고유형대분류코드
    del data['cd_014_lv1']

    data['사고유형중분류코드'] = data['cd_014_lv2']      # 사고유형중분류코드
    del data['cd_014_lv2']

    data['사고유형코드'] = data['cd_014']          # 사고유형코드
    del data['cd_014']

    data['법규위반(1당)대분류코드'] = data['cd_027_1_lv1']    # 법규위반(1당)대분류코드
    del data['cd_027_1_lv1']

    data['법규위반(1당)중분류코드'] = data['cd_027_1_lv2']    # 법규위반(1당)중분류코드
    del data['cd_027_1_lv2']

    data['도로형태대분류코드'] = data['cd_043_lv1']      # 도로형태대분류코드
    del data['cd_043_lv1']

    data['도로형태코드'] = data['cd_043']          # 도로형태코드
    del data['cd_043']

    data['당사자종별(1당)대분류코드'] = data['cd_036_1_lv1']    # 당사자종별(1당)대분류코드
    del data['cd_036_1_lv1']

    data['당사자종별(1당)코드'] = data['cd_036_1']        # 당사자종별(1당)코드
    del data['cd_036_1']

    data['당사자종별(2당)대분류코드'] = data['cd_036_1_lv2']    # 당사자종별(2당)대분류코드
    del data['cd_036_1_lv2']

    data['당사자종별(2당)코드'] = data['cd_036_2']        # 당사자종별(2당)코드
    del data['cd_036_2']

    data['X좌표'] = data['x_coord']         # X 좌표
    del data['x_coord']

    data['Y좌표'] = data['y_coord']         # Y 좌표
    del data['y_coord']

    data['경도'] = data['grd_lo']          # 경도
    del data['grd_lo']

    data['위도'] = data['grd_la']          # 위도
    del data['grd_la']
    return data

def crawling_tad():
    pass