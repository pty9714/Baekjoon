function solution(spell, dic) {
    var answer = 2;

    for (let element of dic) {
        var cnt = 0;

        for (let s of spell) {
            if (!element.includes(s)) {
                break;
            } else {
                cnt += 1;
            }
        }

        if (cnt === spell.length) {
            answer = 1;
            break;
        }
    }

    return answer;
}