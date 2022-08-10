import pandas as pd
import numpy as np
from icecream import ic

import platform
import folium
import json
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from matplotlib import pyplot as plt, font_manager
from matplotlib.pyplot import rc
rc('font', family = font_manager.FontProperties(fname='C:/Windows/Fonts/H2GTRE.ttf').get_name())

from context.domains import Reader, File


class Solution(Reader):
    def __init__(self):
        self.file = File(context='./data/')
        # 먼저 ID 컬럼에서 지도에 표기할때 시 이름 구 이름으로 줄을 나누기 위해 분리한다.
        self.BORDER_LINES = [
            [(5, 1), (5, 2), (7, 2), (7, 3), (11, 3), (11, 0)],  # 인천
            [(5, 4), (5, 5), (2, 5), (2, 7), (4, 7), (4, 9), (7, 9),
             (7, 7), (9, 7), (9, 5), (10, 5), (10, 4), (5, 4)],  # 서울
            [(1, 7), (1, 8), (3, 8), (3, 10), (10, 10), (10, 7),
             (12, 7), (12, 6), (11, 6), (11, 5), (12, 5), (12, 4),
             (11, 4), (11, 3)],  # 경기도
            [(8, 10), (8, 11), (6, 11), (6, 12)],  # 강원도
            [(12, 5), (13, 5), (13, 4), (14, 4), (14, 5), (15, 5),
             (15, 4), (16, 4), (16, 2)],  # 충청북도
            [(16, 4), (17, 4), (17, 5), (16, 5), (16, 6), (19, 6),
             (19, 5), (20, 5), (20, 4), (21, 4), (21, 3), (19, 3), (19, 1)],  # 전라북도
            [(13, 5), (13, 6), (16, 6)],  # 대전시
            [(13, 5), (14, 5)],  # 세종시
            [(21, 2), (21, 3), (22, 3), (22, 4), (24, 4), (24, 2), (21, 2)],  # 광주
            [(20, 5), (21, 5), (21, 6), (23, 6)],  # 전라남도
            [(10, 8), (12, 8), (12, 9), (14, 9), (14, 8), (16, 8), (16, 6)],  # 충청북도
            [(14, 9), (14, 11), (14, 12), (13, 12), (13, 13)],  # 경상북도
            [(15, 8), (17, 8), (17, 10), (16, 10), (16, 11), (14, 11)],  # 대구
            [(17, 9), (18, 9), (18, 8), (19, 8), (19, 9), (20, 9), (20, 10), (21, 10)],  # 부산
            [(16, 11), (16, 13)],  # 울산
            #     [(9,14), (9,15)],
            [(27, 5), (27, 6), (25, 6)],
        ]

    def hook(self):
        def print_menu():
            print('0. Exit')
            print('1. population_raw_data.xlsx 를 읽으시오.')
            print('2. 1번에서 읽은 파일의 "항목" 컬럼을 편집하시오.')
            print('3. 인구 소멸 위기 지역 계산하고 데이터 정리하시오.')
            print('4. 지도 시각화를 위해 지역별 고유 ID를 만드시오.')
            print('5. Cartogram으로 우리나라 지도를 만드시오.')
            print('6. 인구 현황 및 인구 소멸 지역을 확인하시오.')
            print('7. 인구 소멸 위기 지역에 대한 표현하는 지도를 그리시오.')
            print('8. 인구 현황에서 여성 인구 비율을 확인하시오.')
            print('9. 인구 현황에서 2030 여성 인구 비율을 확인하시오.')
            print('10. Folium에서 인구 소멸 위기 지역을 표현하시오.')
            return input('메뉴 선택 \n')

        while 1:
            menu = print_menu()
            if menu == '0':
                break
            elif menu == '1':
                self.preprocessing()
            elif menu == '2':
                self.edit_column()
            elif menu == '3':
                self.organize_data()
            elif menu == '4':
                self.visualize_map()
            elif menu == '5':
                self.cartogram_map()
            elif menu == '6':
                self.drawKorea('인구수합계', self.cartogram_map(), 'Blues')
            elif menu == '7':
                pop = self.cartogram_map()
                pop['소멸위기지역'] = [1 if con else 0 for con in pop['소멸위기지역']]
                self.drawKorea('소멸위기지역', pop, 'Reds')
            elif menu == '8':
                pop = self.cartogram_map()
                pop['여성비'] = (pop['인구수여자'] / pop['인구수합계'] - 0.5) * 100
                self.drawKorea_female('여성비', pop, 'RdBu')
            elif menu == '9':
                pop = self.cartogram_map()
                pop['2030여성비'] = (pop['20-39세여자'] / pop['20-39세합계'] - 0.5) * 100
                self.drawKorea_female('2030여성비', pop, 'RdBu')
            elif menu == '10':
                self.demographic_crisis()

    def preprocessing(self):
        file = self.file
        file.fname = 'population_raw_data'
        population = self.xlsx(file=file, header=1)
        population.fillna(method='pad', inplace=True)
        population.rename(columns={'행정구역(동읍면)별(1)': '광역시도',
                                   '행정구역(동읍면)별(2)': '시도',
                                   '계': '인구수'}, inplace=True)

        population = population[(population['시도'] != '소계')]
        ic(population.head(5))
        return population

    def edit_column(self):
        population = self.preprocessing()
        population.is_copy = False

        population.rename(columns={'항목': '구분'}, inplace=True)

        population.loc[population['구분'] == '총인구수 (명)', '구분'] = '합계'
        population.loc[population['구분'] == '남자인구수 (명)', '구분'] = '남자'
        population.loc[population['구분'] == '여자인구수 (명)', '구분'] = '여자'

        ic(population.head(5))
        population.to_csv('./save/population.csv', index=False)
        return population

    def organize_data(self):
        population = self.edit_column()
        population['20-39세'] = population['20 - 24세'] + population['25 - 29세'] + \
                               population['30 - 34세'] + population['35 - 39세']

        population['65세이상'] = population['65 - 69세'] + population['70 - 74세'] + \
                              population['75 - 79세'] + population['80 - 84세'] + \
                              population['85 - 89세'] + population['90 - 94세'] + \
                              population['95 - 99세'] + population['100+']

        # pivot_table을 이용하여 광역시도, 시도를 index로 두고, 구분으로 세로를 첫 번째 컬럼을 잡고, value에 인구수, 20~39세, 65세이상으로 정리해 둔다.
        pop = pd.pivot_table(population,
                             index=['광역시도', '시도'],
                             columns=['구분'],
                             values=['인구수', '20-39세', '65세이상'])

        # 소멸비율이라는 컬럼에 인구소멸위기지역을 계산하기 위한 식을 적용한다.
        # 이 비율이 1보다 작으면 인구소멸위기지역으로 볼 수 있다.
        pop['소멸비율'] = pop['20-39세', '여자'] / (pop['65세이상', '합계'] / 2)

        # 소멸위기지역인지를 boolean으로 지정해 둔다
        pop['소멸위기지역'] = pop['소멸비율'] < 1.0

        # pivot_table로 잘 정리가 된 상태에서 .reset_index로 pivot_table의 result 속성을 다시 설정한다.
        pop.reset_index(inplace=True)

        # 이중 column을 해제하기 위해 두 컬럼 제목을 합쳐 다시 지정한다.
        tmp_coloumns = [pop.columns.get_level_values(0)[n] + \
                        pop.columns.get_level_values(1)[n]
                        for n in range(0, len(pop.columns.get_level_values(0)))]
        pop.columns = tmp_coloumns
        ic(pop.info())
        return pop

    def visualize_map(self):
        pop = self.organize_data()
        pop['시도'].unique()

        si_name = [None] * len(pop)

        tmp_gu_dict = {'수원': ['장안구', '권선구', '팔달구', '영통구'],
                       '성남': ['수정구', '중원구', '분당구'],
                       '안양': ['만안구', '동안구'],
                       '안산': ['상록구', '단원구'],
                       '고양': ['덕양구', '일산동구', '일산서구'],
                       '용인': ['처인구', '기흥구', '수지구'],
                       '청주': ['상당구', '서원구', '흥덕구', '청원구'],
                       '천안': ['동남구', '서북구'],
                       '전주': ['완산구', '덕진구'],
                       '포항': ['남구', '북구'],
                       '창원': ['의창구', '성산구', '진해구', '마산합포구', '마산회원구'],
                       '부천': ['오정구', '원미구', '소사구']}

        for n in pop.index:
            if pop['광역시도'][n][-3:] not in ['광역시', '특별시', '자치시']:
                if pop['시도'][n][:-1] == '고성' and pop['광역시도'][n] == '강원도':
                    si_name[n] = '고성(강원)'
                elif pop['시도'][n][:-1] == '고성' and pop['광역시도'][n] == '경상남도':
                    si_name[n] = '고성(경남)'
                else:
                    si_name[n] = pop['시도'][n][:-1]

                for keys, values in tmp_gu_dict.items():
                    if pop['시도'][n] in values:
                        if len(pop['시도'][n]) == 2:
                            si_name[n] = keys + ' ' + pop['시도'][n]
                        elif pop['시도'][n] in ['마산합포구', '마산회원구']:
                            si_name[n] = keys + ' ' + pop['시도'][n][2:-1]
                        else:
                            si_name[n] = keys + ' ' + pop['시도'][n][:-1]

            elif pop['광역시도'][n] == '세종특별자치시':
                si_name[n] = '세종'

            else:
                if len(pop['시도'][n]) == 2:
                    si_name[n] = pop['광역시도'][n][:2] + ' ' + pop['시도'][n]
                else:
                    si_name[n] = pop['광역시도'][n][:2] + ' ' + pop['시도'][n][:-1]

        # ic(si_name)

        # 지도 시각화에 사용하기 위해 위 과정에서 만들어진 행정구역의 고유한 이름을 ID로 지정한다.
        pop['ID'] = si_name
        del pop['20-39세남자']
        del pop['65세이상남자']
        del pop['65세이상여자']

        ic(pop.head(5))
        return pop

    def cartogram_map(self):
        pop = self.visualize_map()
        file = self.file
        file.fname = 'draw_korea_raw'
        draw_korea_raw = self.xlsx(file=file, header=0)
        # ic(draw_korea_raw.head(5))

        # 이제 각 행정 구역의 화면상 좌표를 얻기 위해 pivot_table의 반대 개념으로 .stack() 명령을 사용한다.
        draw_korea_raw_stacked = pd.DataFrame(draw_korea_raw.stack())
        draw_korea_raw_stacked.reset_index(inplace=True)
        draw_korea_raw_stacked.rename(columns={'level_0': 'y', 'level_1': 'x', 0: 'ID'},
                                      inplace=True)
        ic(draw_korea_raw_stacked)

        # 인덱스를 재설정하고 컬럼의 이름을 다시 설정해 준다.
        draw_korea = draw_korea_raw_stacked

        plt.figure(figsize=(8, 11))

        # 지역 이름 표시
        for idx, row in draw_korea.iterrows():

            # 광역시는 구 이름이 겹치는 경우가 많아서 시단위 이름도 같이 표시한다.
            # (중구, 서구)
            if len(row['ID'].split()) == 2:
                dispname = '{}\n{}'.format(row['ID'].split()[0], row['ID'].split()[1])
            elif row['ID'][:2] == '고성':
                dispname = '고성'
            else:
                dispname = row['ID']

            # 서대문구, 서귀포시 같이 이름이 3자 이상인 경우에 작은 글자로 표시한다.
            if len(dispname.splitlines()[-1]) >= 3:
                fontsize, linespacing = 9.5, 1.5
            else:
                fontsize, linespacing = 11, 1.2

            plt.annotate(dispname, (row['x'] + 0.5, row['y'] + 0.5), weight='bold',
                         fontsize=fontsize, ha='center', va='center',
                         linespacing=linespacing)

        # 시도 경계 그린다.
        for path in self.BORDER_LINES:
            ys, xs = zip(*path)
            plt.plot(xs, ys, c='black', lw=1.5)

        plt.gca().invert_yaxis()
        # plt.gca().set_aspect(1)

        plt.axis('off')

        plt.tight_layout()
        plt.rc('axes', unicode_minus=False)
        plt.show()

        # ic(pop)

        # 인구에 대한 분석 결과인 pop과 지도를 그리기 위한 draw_korea의 대이터를 합칠 때 사용할 key인 ID 컬럼의 내용이 문제가 없는지 확인하자.
        set(draw_korea['ID'].unique()) - set(pop['ID'].unique())  # set()
        set(pop['ID'].unique()) - set(draw_korea['ID'].unique())  # {'청주', '전주', '안양', '창원', '포항', '천안', '부천', '안산', '성남', '고양', '수원', '용인'}

        # 위 결과에 따르면, pop에 행정구를 가진 시들의 데이터가 더 있다는 것을 알 수 있다.
        # 어차피 지도에서는 표시되지 못하니 삭제한다.
        tmp_list = list(set(pop['ID'].unique()) - set(draw_korea['ID'].unique()))

        for tmp in tmp_list:
            pop = pop.drop(pop[pop['ID'] == tmp].index)

        set(pop['ID'].unique()) - set(draw_korea['ID'].unique())  # set()

        # ic(pop.head(5))

        # 이제 pop과 draw_korea의 ID 컬럼이 일치했다고 보고, ID를 key로 merge를 시키도록 한다.
        pop = pd.merge(pop, draw_korea, how='left', on=['ID'])
        # ic(pop.head(5))

        # 이제 위 pop 데이터에서 지도에 표현하고자 하는 데이터가 인구수합계라면 이 값들이 아까 만든 각 해당 행정구역에 위치하면 된다.
        mapdata = pop.pivot_table(index='y', columns='x', values='인구수합계')
        masked_mapdata = np.ma.masked_where(np.isnan(mapdata), mapdata)
        ic(mapdata)
        ic(masked_mapdata)

        draw_korea.to_csv("./save/draw_korea.csv", encoding='utf-8', sep=',')
        pop.to_csv('./save/pop.csv', index=False)
        return pop

    def drawKorea(self, targetData, blockedMap, cmapname):
        gamma = 0.75

        whitelabelmin = (max(blockedMap[targetData]) -
                         min(blockedMap[targetData])) * 0.25 + \
                        min(blockedMap[targetData])

        datalabel = targetData

        vmin = min(blockedMap[targetData])
        vmax = max(blockedMap[targetData])

        mapdata = blockedMap.pivot_table(index='y', columns='x', values=targetData)
        masked_mapdata = np.ma.masked_where(np.isnan(mapdata), mapdata)

        plt.figure(figsize=(9, 11))
        plt.pcolor(masked_mapdata, vmin=vmin, vmax=vmax, cmap=cmapname,
                   edgecolor='#aaaaaa', linewidth=0.5)

        # 지역 이름 표시
        for idx, row in blockedMap.iterrows():
            # 광역시는 구 이름이 겹치는 경우가 많아서 시단위 이름도 같이 표시한다.
            # (중구, 서구)
            if len(row['ID'].split()) == 2:
                dispname = '{}\n{}'.format(row['ID'].split()[0], row['ID'].split()[1])
            elif row['ID'][:2] == '고성':
                dispname = '고성'
            else:
                dispname = row['ID']

            # 서대문구, 서귀포시 같이 이름이 3자 이상인 경우에 작은 글자로 표시한다.
            if len(dispname.splitlines()[-1]) >= 3:
                fontsize, linespacing = 10.0, 1.1
            else:
                fontsize, linespacing = 11, 1.

            annocolor = 'white' if row[targetData] > whitelabelmin else 'black'
            plt.annotate(dispname, (row['x'] + 0.5, row['y'] + 0.5), weight='bold',
                         fontsize=fontsize, ha='center', va='center', color=annocolor,
                         linespacing=linespacing)
        self.draw_border_lines(datalabel)

    def drawKorea_female(self, targetData, blockedMap, cmapname):
        gamma = 0.75

        whitelabelmin = 20.

        datalabel = targetData

        tmp_max = max([np.abs(min(blockedMap[targetData])),
                       np.abs(max(blockedMap[targetData]))])
        vmin, vmax = -tmp_max, tmp_max

        mapdata = blockedMap.pivot_table(index='y', columns='x', values=targetData)
        masked_mapdata = np.ma.masked_where(np.isnan(mapdata), mapdata)

        plt.figure(figsize=(9, 11))
        plt.pcolor(masked_mapdata, vmin=vmin, vmax=vmax, cmap=cmapname,
                   edgecolor='#aaaaaa', linewidth=0.5)

        # 지역 이름 표시
        for idx, row in blockedMap.iterrows():
            # 광역시는 구 이름이 겹치는 경우가 많아서 시단위 이름도 같이 표시한다.
            # (중구, 서구)
            if len(row['ID'].split()) == 2:
                dispname = '{}\n{}'.format(row['ID'].split()[0], row['ID'].split()[1])
            elif row['ID'][:2] == '고성':
                dispname = '고성'
            else:
                dispname = row['ID']

            # 서대문구, 서귀포시 같이 이름이 3자 이상인 경우에 작은 글자로 표시한다.
            if len(dispname.splitlines()[-1]) >= 3:
                fontsize, linespacing = 10.0, 1.1
            else:
                fontsize, linespacing = 11, 1.

            annocolor = 'white' if np.abs(row[targetData]) > whitelabelmin else 'black'
            plt.annotate(dispname, (row['x'] + 0.5, row['y'] + 0.5), weight='bold',
                         fontsize=fontsize, ha='center', va='center', color=annocolor,
                         linespacing=linespacing)
        self.draw_border_lines(datalabel)

    def draw_border_lines(self, datalabel):
        # 시도 경계 그린다.
        for path in self.BORDER_LINES:
            ys, xs = zip(*path)
            plt.plot(xs, ys, c='black', lw=2)

        plt.gca().invert_yaxis()

        plt.axis('off')

        cb = plt.colorbar(shrink=.1, aspect=10)
        cb.set_label(datalabel)

        plt.tight_layout()
        plt.rc('axes', unicode_minus=False)
        plt.show()

    def demographic_crisis(self):
        pop = self.cartogram_map()
        pop['여성비'] = (pop['인구수여자'] / pop['인구수합계'] - 0.5) * 100
        pop['2030여성비'] = (pop['20-39세여자'] / pop['20-39세합계'] - 0.5) * 100
        pop.to_csv('./save/pop.csv', index=False)
        pop_folium = pop.set_index('ID')
        file = self.file
        file.fname = 'skorea_municipalities_geo_simple'
        geo_str = self.map_json(file)

        pop_sum_map = folium.Map(location=[36.2002, 127.054], zoom_start=7)
        pop_sum_map.choropleth(geo_data=geo_str,
                       data=pop_folium['인구수합계'],
                       columns=[pop_folium.index, pop_folium['인구수합계']],
                       fill_color='YlGnBu',  # PuRd, YlGnBu
                       key_on='feature.id')

        pop_sum_map.save('./save/pop_sum_map.html')

        extinction_danger_map = folium.Map(location=[36.2002, 127.054], zoom_start=7)
        extinction_danger_map.choropleth(geo_data=geo_str,
                       data=pop_folium['소멸위기지역'],
                       columns=[pop_folium.index, pop_folium['소멸위기지역']],
                       fill_color='PuRd',  # PuRd, YlGnBu
                       key_on='feature.id')
        extinction_danger_map.save('./save/extinction_danger_map.html')


if __name__ == '__main__':
    Solution().hook()