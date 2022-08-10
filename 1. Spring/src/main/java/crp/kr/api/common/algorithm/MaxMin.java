package crp.kr.api.common.algorithm;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.junit.jupiter.api.Test;

/**
 * packageName:crp.kr.api.common.algorithm
 * fileName        :MaxMin
 * author           : chohyungook
 * date               :2022-05-17
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-17chohyungook최초 생성
 */
/*
    그리디와 완전탐색
    공통점 : 선형 구조, for loop 사용
    차이점 : if문 사용 → 더 나은 상황인지 몰라도 실행
    cf. 비선형구조는 그래프와 트리
 */
public class MaxMin {
    @Builder
    @NoArgsConstructor
    @AllArgsConstructor
    @Getter
    public static class Solution {
        private int[] arr;
        private int max, min; // 속성 → 빌더

        @Override
        public String toString() {
            return String.format("min = %d, max = %d", min, max);
        }
    }

    @FunctionalInterface private interface SolutionService {
        public Solution solution(Solution s);
    }

    @Test
    void testSolution() {
        int[] arr = {3, 1, 9, 5, 10}; // 더미
        SolutionService f = e -> {
            int min = 10, max = 0;
            for (int i : e.getArr()) {
                if (i < min) min = i;
                if (i > max) max = i;
            }
            return Solution.builder().min(min).max(max).build();
        };
        Solution s = Solution.builder().arr(arr).build();
        System.out.println(f.solution(s));
    }
}