package crp.kr.api.common.algorithm;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

/**
 * packageName:crp.kr.api.common.algorithm
 * fileName        :PrimeNumber
 * author           : chohyungook
 * date               :2022-05-17
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-17chohyungook최초 생성
 */
public class PrimeNumber {
    @Data
    @Builder
    @NoArgsConstructor
    @AllArgsConstructor
    private static class Prime{
        private int start,end;
        private int[] primes;

        @Override
        public String toString() {
            int count=0;
            for (int i=2; i<=100;i++){
                for(int j =2; j<=i; j++){
                    if(i%j==0) {
                        count++;
                    }
                }
                if (count==1){
                    System.out.println(i+"");
                }
                count=0;
            }

            return String.format("소수: %d",primes);
        }
        @FunctionalInterface private interface SolutionService1{
            String solution1(List<?> list);
        }
        @Test
        void testSolution(){
            List<Integer> list = Arrays.asList(1,2,3,4,5,6,7,8,9,10);
            SolutionService1 sol = x -> "";
            System.out.println(sol.solution1(list));
        }
    }
}
