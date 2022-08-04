package crp.kr.api.common.algorithm;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.junit.jupiter.api.Test;

import java.util.Arrays;

/**
 * packageName:crp.kr.api.common.algorithm
 * fileName        :RemoveDuplicatedElementsArray
 * author           : chohyungook
 * date               :2022-05-17
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-17chohyungook최초 생성
 */
public class RemoveDuplicatedElementsArray {
    @Builder @Getter @AllArgsConstructor @NoArgsConstructor
    static class DuplicatedArray{
        private int[] arr;
        private int[] result;

        @Override
        public String toString() {
            return String.format("중복배열이 제거된 새 배열 : %d",result);
        }
        @FunctionalInterface private interface DuplicatedArrayService{
            DuplicatedArray dupl(DuplicatedArray d);
        }
        @Test
        void DuplicatedArrayTest(){
            int[] arr = {5,10,9,27,2,8,10,4,27,1};
            int[] result = new int[10];
            DuplicatedArrayService da= e ->{
                Arrays.stream(arr).distinct().toArray();
                return DuplicatedArray.builder().result(result).build();
            };
            DuplicatedArray d = DuplicatedArray.builder().arr(arr).build();
            System.out.println(da.dupl(d));
        }
    }


}
