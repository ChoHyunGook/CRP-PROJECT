package crp.kr.api.common.streams;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.junit.jupiter.api.Test;

import java.text.SimpleDateFormat;
import java.util.Arrays;
import java.util.Date;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

/**
 * packageName:crp.kr.api.common.streams
 * fileName        :PersonStream
 * author           : chohyungook
 * date               :2022-05-16
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-16chohyungook최초 생성
 */
public class PersonStream {
    @Data
    @Builder
    @NoArgsConstructor
    @AllArgsConstructor
    public static class Person{
        private String name,ssn;
        @Override public String toString(){
            int a = Integer.parseInt(ssn.substring(ssn.length()-1));
            int b = Integer.parseInt(new SimpleDateFormat("YY").format(new Date()));
            int c = Integer.parseInt(ssn.substring(0,2));
            String gender=(ssn.substring(7).equals("1")||ssn.substring(7).equals("3"))?"남자":"여자";
            int age = a / 2 == 0 ? (100 + b - c) : (b - c) ;
            return String.format("이름: %s, 성별: %s, 나이: %d",name,gender,age);
        }
    }

    // 기능:회원검색
    @FunctionalInterface/*람다*/ interface PersonService{ Person search(List<Person>/*임마가 e다*/ arr/*임마가 b다*/);}

    @Test
    void personStreamTest(){
        //홍길동,900101-1
        //김유신,950101-1
        //유관순,040203-4
        //남성,여성 판단 로직
        List<Person> arr = Arrays.asList(
                Person.builder().name("홍길동").ssn("900101-1").build(),
                Person.builder().name("김유신").ssn("950101-1").build(),
                Person.builder().name("유관순").ssn("040203-4").build()
        );
        PersonService ps = b -> b
                .stream()//공중에 띄워서
                        .filter(e/*임마가 List<Person>*/->e.getName().equals("홍길동"))//얘만
                                .collect(Collectors.toList()).get(0);//컨택을 하고
        System.out.println(ps.search(arr));;//남겨서 보여주고! 끝나면 없어짐.
    }

}
