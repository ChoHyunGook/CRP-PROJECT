package crp.kr.api.common.lambdas;

import java.io.File;
import java.time.LocalDate;
import java.util.function.BiFunction;
import java.util.function.BiPredicate;
import java.util.function.Function;
import java.util.function.Supplier;

/**
 * packageName:crp.kr.api.common.lambda
 * fileName        :Lambda
 * author           : chohyungook
 * date               :2022-05-11
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-11chohyungook최초 생성
 */
public class Lambda {
    public static void main(String[] args) {
/*        System.out.println(Lambda.integer("900"));
        System.out.println(Lambda.string(900));
        System.out.println(string(new Apple.Builder().origin("영동").color("RED").price(3000).build()));
        System.out.println(string(
                Arrays.asList(
                        new Apple.Builder().origin("영동").color("RED").price(3000).build(),
                        new Apple.Builder().origin("영동").color("BLUE").price(3000).build(),
                        new Apple.Builder().origin("풍기").color("BLUE").price(3000).build()
                )
        ));
        System.out.println(equals("홍길동", "홍"));
        System.out.println(equals("홍길동", "홍길동"));
        System.out.println(array(8).length);*/
        System.out.println(random(1,6));
    }
    public static long longParse(String s){
        Function<String, Long> f = Long::parseLong;
        return f.apply(s);
    }
    public static float floatParse(String s){
        Function<String,Float> f = Float::parseFloat;
        return f.apply(s);
    }
    public static int integer(String arg) {
//        Integer i = Integer.parseInt("900")
        Function<String, Integer> f = Integer::parseInt; // <파라미터타입, 리턴타입> // :: 메소드 참조
        return f.apply(arg);
    }

    public static String string(Object o) {
//        String s = String.valueOf(o); // JSON.stringify()
        Function<Object, String> f = String::valueOf;
        return f.apply(o);
    }

    public static boolean equals(String s1, String s2) {
//        boolean b = "홍길동".equals("홍%");
        BiPredicate<String, String> p = String::equals; // Predicate은 이미 리턴타입이 boolean으로 fix Bi는 2개인자받는
        return p.test(s1, s2);
    }

    //    int[] arr = new int[8];
//    int 타입의 size를 파라미터로 던지면 arr가 생성됨
    public static int[] array(Integer i) {
        Function<Integer, int[]> f = int[]::new;
        return f.apply(i);
    }

    public static int random(int min, int max) {
        BiFunction<Integer,Integer,Integer> d = (a,b) -> (int)(Math.random()*b)+a;
        return d.apply(min,max);
        //Supplier<Double> d = Math::random;
        //return (int)(d.get()*max)+min;
    }

    public static File file(String s){
        Function<String,File> a = File::new;
        return a.apply(s);
    }
    public static String date(){
        Supplier<String> f = () -> string(LocalDate.now());
        return f.get();
    }
}
