package crp.kr.api.common.algorithm;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.junit.jupiter.api.Test;

import java.util.Arrays;

/**
 * packageName:crp.kr.api.common.algorithm
 * fileName        :CheckSameArray
 * author           : chohyungook
 * date               :2022-05-17
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-17chohyungook최초 생성
 */
public class CheckSameArray {
    @Builder @Getter @AllArgsConstructor @NoArgsConstructor
    static class CheckSame{
        private int[] arr1;
        private int[] arr2;
        boolean result;

        @Override
        public String toString() {
            return String.format("%s",result);
        }
    }
    @FunctionalInterface private interface CheckSameService{
        CheckSame check(CheckSame c);
    }
    @Test
    void CheckSameTest(){
        int[] arr1 = {1,3,2};
        int[] arr2 = {2,3,1};
        boolean result;
        CheckSameService s = e ->{
            Arrays.equals(Arrays.stream(arr1).toArray(),Arrays.stream(arr2).toArray());
          return CheckSame.builder().build();
        };
        CheckSame c = CheckSame.builder().build();
        System.out.println(s.check(c));
    }
}
