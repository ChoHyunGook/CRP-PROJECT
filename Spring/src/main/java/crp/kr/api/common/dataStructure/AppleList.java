package crp.kr.api.common.dataStructure;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

import static crp.kr.api.common.lambdas.Lambda.array;
import static crp.kr.api.common.lambdas.Lambda.integer;

/**
 * packageName:crp.kr.api.common.dataStructure
 * fileName        :AppleList
 * author           : chohyungook
 * date               :2022-05-11
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-11chohyungook최초 생성
 */
public class AppleList {
    @Data
    public static class Apple{
        private String color, origin;
        private int price;

        public Apple(Builder builder) {
            this.color = builder.color;
            this.origin = builder.origin;
            this.price = builder.price;
        }
        @NoArgsConstructor static public class Builder{
            private String color, origin;
            private int price;
            public Builder color(String color){this.color=color; return this;}
            public Builder origin(String origin){this.origin=origin; return this;}
            public Builder price(int price){this.price=price; return this;}
            public Apple build(){ return new Apple(this);}
        }
        @Override public String toString(){
            return String.format("[사과 스펙] origin: %s, color: %s, price: %d",
                    origin, color, price);
        }
    }
    interface AppleService{
        void save(Apple apple);
        void update(int i, Apple apple);
        void delete(Apple apple);
        List<Apple> findAll();
        List<Apple> findByOrigin(String origin);
        List<Apple> findByColor(String color);
        Apple findById(int i);
        int countAll();
        void clear();
    }
    static class AppleServiceImpl implements AppleService{
        private final List<Apple> list;

        public AppleServiceImpl() {
            this.list = new ArrayList<>();
        }

        @Override
        public void save(Apple apple) {
            list.add(apple);
        }

        @Override
        public void update(int i, Apple apple) {
            list.set(i,apple);
        }

        @Override
        public void delete(Apple apple) {
            list.remove(apple);
        }

        @Override
        public List<Apple> findAll() {
            return list;
        }

        @Override
        public List<Apple> findByOrigin(String origin) {
            return list.stream()
                    .filter(apple -> apple.getOrigin().equals(origin))
                    .collect(Collectors.toList());

        }

        @Override
        public List<Apple> findByColor(String color) {
            return null;
        }

        @Override
        public Apple findById(int i) {
            return list.get(i);
        }

        @Override
        public int countAll() {
            return list.size();
        }

        @Override
        public void clear() {
            list.clear();
        }
    }
    @Test
    void appleAppTest(){
        AppleService service = new AppleServiceImpl();
        System.out.println("### 1. save ###");
        Apple yd = new Apple.Builder()
                .origin("영동")
                .color("RED")
                .price(1000)
                .build();
        service.save(yd);
        Apple yd2 = new Apple.Builder()
                .origin("영동")
                .color("BLUE")
                .price(1500)
                .build();
        service.save(yd2);
        Apple pg = new Apple.Builder()
                .origin("풍기")
                .color("RED")
                .price(2000)
                .build();
        service.save(pg);
        System.out.println("### 2. countAll ###");
        System.out.println(service.countAll());
        System.out.println("### 3. findAll ###");
        System.out.println(service.findAll());
        System.out.println("### 4. findByOrigin ###");
        System.out.println(service.findByOrigin("영동"));
        System.out.println("### 5. findById ###");
        System.out.println("첫번째 사과정보:" +service.findById(0));
        System.out.println("### 6. update ###");
        service.update(0, new Apple.Builder()
                .origin("캘리포니아")
                .color("YELLOW")
                .price(20000)
                .build());
        System.out.println("수정된 사과정보:" +service.findById(0));
        System.out.println("### 7. delete ###");
        service.delete(new Apple.Builder()
                .origin("캘리포니아")
                .color("YELLOW")
                .price(20000)
                .build());
        System.out.println("삭제후 카운트 감소확인: "+service.countAll());
        System.out.println("### 8. clear ###");
        service.clear();
        System.out.println("clear 후 카운트 0 확인: "+ service.countAll());

    }
}
