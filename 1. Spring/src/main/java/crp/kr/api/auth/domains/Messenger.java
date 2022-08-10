package crp.kr.api.auth.domains;

import lombok.Builder;
import lombok.Getter;

/**
 * packageName:crp.kr.api.security.domains
 * fileName        :Messenger
 * author           : chohyungook
 * date               :2022-05-23
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-23chohyungook최초 생성
 */
@Getter @Builder
public class Messenger {
    private String message,code,token;
    private int status;
}
