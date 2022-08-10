package crp.kr.api.auth.exception;

/**
 * packageName:crp.kr.api.auth.exception
 * fileName        :ErrorCode
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
@Getter
@RequiredArgsConstructor
public enum ErrorCode {
    AUTHENTICATION_FAILED(401, "AUTH_001", "AUTHENTICATION_FAILED"),
    LOGIN_FAILED(401, "AUTH_002", "LOGIN_FAILED"),
    ACCESS_DENIED(401, "AUTH_003", "ACCESS_DENIED"),
    TOKEN_GENERATION_FAILED(500, "AUTH_004", "TOKEN_GENERATION_FAILED");
    private final int status;
    private final String code;
    private final String msg;
}
