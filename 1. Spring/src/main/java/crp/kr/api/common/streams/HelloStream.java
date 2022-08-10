package crp.kr.api.common.streams;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

/**
 * packageName:crp.kr.api.common.streams
 * fileName        :HelloStream
 * author           : chohyungook
 * date               :2022-05-16
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-16chohyungook최초 생성
 */
//한국어 안녕, 영어 Hello
public class HelloStream {
    @Data
    @Builder
    @NoArgsConstructor
    @AllArgsConstructor
    public static class Hello{
        private String greeting, inLanguage;

        @Override public String toString(){
            return String.format("[언어 스펙] greeting: %s, inLanguage: %s",
                    greeting,inLanguage);
        }
    }
   interface HelloService{
       Set<Hello> greet(List<Hello> arr);
   }
    static class HelloServiceImpl implements HelloService{
        @Override
        public Set<Hello> greet(List<Hello> arr) {
            return arr
                    .stream()
                    .filter(e->e.getInLanguage().equals("영어"))
                    .collect(Collectors.toSet());
        }
    }
    @Test
    void HelloStreamTest(){
       List<Hello> arr = Arrays.asList(
               Hello.builder().inLanguage("영어").greeting("Hello").build(),
               Hello.builder().inLanguage("한국어").greeting("안녕").build()
       );
       new HelloServiceImpl().greet(arr).forEach(System.out::print);

    }


}

