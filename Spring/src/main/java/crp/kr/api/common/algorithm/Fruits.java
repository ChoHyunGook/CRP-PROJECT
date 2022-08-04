package crp.kr.api.common.algorithm;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.junit.jupiter.api.Test;

import java.util.Arrays;

/**
 * packageName:crp.kr.api.common.algorithm
 * fileName        :Fruits
 * author           : chohyungook
 * date               :2022-05-17
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-17chohyungook최초 생성
 */
public class Fruits {
    @Builder
    @Getter
    @NoArgsConstructor
    @AllArgsConstructor
    static class Fruit {
        private int apple, grape, orange;
        private int[][] price;
        private int total;

        @Override
        public String toString() {
            return String.format("총합: %d, 사과평균: %d, 포도평균: %d, 오렌지평균: %d",
                    total, apple, grape, orange);
        }
    }
        @FunctionalInterface private interface FruitService{
            Fruit fruit(Fruit f);
        }
        @Test
        void FruitsTest(){
            int[][] price ={{10000,20000,12000},{8000,3000,15000},{20000,15000,38000},{13000,20000,30000}
                    ,{30000,12000,20000},{35000,30000,25000},{50000,23000,10000}};
            FruitService d = e ->{
                int total=0;
                int apple=0;
                int grape=0;
                int orange=0;
                for(int i =0; i< price.length; i++){
                    for(int j =0; j< price[i].length; j++){
                        if(j==0){
                            apple += price[i][j];
                        }else if (j==1){
                            grape += price[i][j];
                        }else{
                            orange += price[i][j];
                        }
                        total += price[i][j];
                    }
                }
                apple=apple/price.length;
                grape=grape/price.length;
                orange=orange/price.length;
                return Fruit.builder()
                        .apple(apple).grape(grape).orange(orange).total(total).build();
            };
            Fruit f = Fruit.builder().price(price).build();
            System.out.println(d.fruit(f));
        }
    }

