function solution(array) {
    const map = {};

    for (const n of array) {
        map[n] = (map[n] || 0) + 1;
    }

    // 빈 배열 처리
    if (Object.keys(map).length === 0) {
        return -1;  // 만약 배열이 비어 있으면 -1을 반환
    }

    const sorted = Object.entries(map).sort((a, b) => b[1] - a[1]);

    // 배열에 원소가 하나일 경우 바로 반환
    if (array.length === 1) {
        return array[0];
    }

    // 가장 빈도가 높은 값이 두 개 이상인 경우
    if (sorted.length > 1 && sorted[0][1] === sorted[1][1]) {
        return -1;
    }

    // 최빈값을 반환 (key는 문자열이므로 숫자로 변환)
    return Number(sorted[0][0]);
}
