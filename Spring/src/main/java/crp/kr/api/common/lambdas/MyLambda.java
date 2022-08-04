package crp.kr.api.common.lambdas;

/**
 * packageName:crp.kr.api.common.lambda
 * fileName        :MyLambda
 * author           : chohyungook
 * date               :2022-05-13
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-13chohyungook최초 생성
 */
public class MyLambda {
    @FunctionalInterface interface MyFunction{int execute(String arg);}
    @FunctionalInterface interface MySupplier{int execute();}
    @FunctionalInterface interface MyConsumer{void execute(String arg);}
    @FunctionalInterface interface MyPredicate{boolean execute(String arg);}
    @FunctionalInterface interface MyInterface{String myMethod();}
    @FunctionalInterface interface MyUnaryOp{int operator(Integer a);}
    @FunctionalInterface interface LengthOfString{int excute(String arg);}//id password 길이 제한할때
    @FunctionalInterface interface MathOperation{int excute(int a , int b);}
}
