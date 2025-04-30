function solution(my_string) {
    return my_string
        .split('')                      // 문자열을 한 글자씩 나눔
        .filter(char => !isNaN(char) && char !== ' ')  // 숫자인 문자만 필터링
        .map(Number)                   // 숫자로 변환
        .sort((a, b) => a - b);        // 오름차순 정렬
}