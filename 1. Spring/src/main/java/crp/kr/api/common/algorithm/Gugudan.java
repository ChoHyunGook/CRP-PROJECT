package crp.kr.api.common.algorithm;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.junit.jupiter.api.Test;

import java.util.stream.IntStream;

/**
 * packageName:crp.kr.api.common.algorithm
 * fileName        :Gugudan
 * author           : chohyungook
 * date               :2022-05-17
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-17chohyungook최초 생성
 */
public class Gugudan {//완전탐색
    @Builder @Getter @NoArgsConstructor @AllArgsConstructor
    static class Solution{
        private int num ;
        private String result;
        @Override
        public String toString() {
            return result ;
        }
    }
    @Getter @AllArgsConstructor @NoArgsConstructor @Builder
    static class JinyoungSolution{
        private String result;
        private int num;
        @Override
        public String toString() {
            return result;
        }
    }
    @FunctionalInterface interface ISolution{ Solution solution(Solution s);}
    @FunctionalInterface interface IMinseoGugudan{ void solution();}
    @FunctionalInterface interface IJinyoungGugudan{ JinyoungSolution solution(JinyoungSolution s);}
    @FunctionalInterface interface IHyungukSolution{ void solution();}
    static class Service{
        static IMinseoGugudan iMinseo = ()-> {
            int i = 0, j = 0;
            for ( i = 1; i < 10; i++) {
                for ( j = 2; j < 6; j++) {
                    System. out.print( j + "*" + i + "=" + i * j + "\t");
                }
                System. out.println();
            }
            System. out.println();
            for ( i = 1; i < 10; i++) {
                for ( j = 6; j < 10; j++) {
                    System. out.print( j + "*" + i + "=" + i * j + "\t");
                }
                System. out.println();
            }
        };
        static IJinyoungGugudan iJinyoung = e -> {
            String result = "";
            for(int k = 2; k <= e.getNum(); k+=4) {
                for (int i = 1; i <= e.getNum(); i++) {
                    for (int j = k; j < k+4; j++) {
                        result +=  j + "*" + i+ "=" +(j*i)+"\t";
                    }
                    result += '\n';
                }
                result += '\n';
            }
            return JinyoungSolution.builder().result(result).build();
        };
        static ISolution iSolution = e ->{
            int[][] arr = new int[e.getNum()][e.getNum()];
            String result = "";
            for(int i=0; i< arr.length-1; i++){
                for(int j=0; j< arr[i].length; j++){
                    arr[i][j] = (i+2) * (j+1);
                    result += String.format("%d * %d = %d\n", i+2, j+1, arr[i][j]);
                }
                result += '\n';
            }
            return Solution.builder().result(result).build();
        };
        static IHyungukSolution iHyunguk = () ->{
            IntStream.rangeClosed(2,9).forEach(i->{
                IntStream.rangeClosed(1,9).forEach(j->{
                    System.out.print(i + "*" + j + "=" + String.format("%2d",i * j));
                    System.out.print("   ");
                });
                System.out.println();
            });
        };
    }
    @Test
    void test(){
        // 기본형 구구단
        // Service.iMinseo.solution();
        // 이차원배열. 구구단 정렬 무시
        // System.out.println(Service.iSolution.solution(Solution.builder().num(19).build()));
        // 책받침 구구단
        // System.out.println(Service.iJinyoung.solution(JinyoungSolution.builder().num(19).build()));
        // 람다 구구단
        Service.iHyunguk.solution();
    }
/*
    @FunctionalInterface private interface GugudanService{
        void gugu();
    }
    @Test
    void GuguTest(){
        IntStream.rangeClosed(2,9).forEach(i->{
            IntStream.rangeClosed(1,9).forEach(j->{
                System.out.print(i + "*" + j + "=" + String.format("%2d",i * j));
                System.out.print("   ");
            });
            System.out.println();
        });
    }*/
}
