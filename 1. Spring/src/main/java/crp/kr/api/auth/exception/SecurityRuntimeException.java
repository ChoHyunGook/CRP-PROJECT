package crp.kr.api.auth.exception;

/**
 * packageName:crp.kr.api.auth.exception
 * fileName        :SecurityRuntimeException
 * author           : chohyungook
 * date               :2022-05-25
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-25chohyungook최초 생성
 */
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;

@Getter
@RequiredArgsConstructor
public class SecurityRuntimeException extends RuntimeException{
    private static final long SerializableUID = 1L;

    private final String msg;
    private final HttpStatus httpStatus;
}
