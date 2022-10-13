#2022/10/11

#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
travel_log = {
    "France": { "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 23},
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
} 

LoveDate_log = {
    "Gwangju": { "cities_visited": ["Dongmeong-Dong", "MaeGok-Dong", "ChungJang-lo", "SsangChon-Dong"], "total_visited": 3},
    "Busan": ["Bexco", "GwangAn-li"]
}


#Nesting Dictionay in a list 
# 문자열, 리스트, 정수를 가진 2개의 딕셔너리를 가진 리스트
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 5
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 10
    } 
]