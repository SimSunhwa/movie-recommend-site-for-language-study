# 난이도 있는 영화들 총 1860개  
# 1860개 csv 데이터만 movies.json으로 변환 시키기 

import csv
import json

# CSV 파일 경로
csv_file_path = 'filtered_2_300.csv'
json_file_path = 'movies.json'

# JSON 변환에 필요한 모델 이름 지정
model_name = 'movies.movie'

# JSON 데이터 저장 리스트
json_data = []

# CSV 파일 읽기
with open('filtered_2_300.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    
    pk = 1
    for row in reader:
        # 각 row를 Django JSON 구조로 변환 , 필드 총 11개
        movie_data = {
            "model": model_name,
            "pk": pk,
            "fields": {
                "tmdb_id": int(row["tmdbid"]),
                "title": row["title"],
                "title_kr": '',
                "rank": float(row["rank"]),
                "release_date": row["release_date"],
                "runtime":int(row["runtime"]),
                "summary": row["summary"],
                "production": row["production"],
                "country":row["country"],
                "poster_path": row["poster_path"],
                "is_adult": False,
                "difficulty": row["study_level"]
            }
        }
        json_data.append(movie_data)
        pk += 1

# JSON 파일로 저장
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=4, separators=(',', ': '))
