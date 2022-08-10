package crp.kr.api.user.domains;

import lombok.Getter;
import lombok.RequiredArgsConstructor;
import org.springframework.security.core.GrantedAuthority;

import java.util.Arrays;

/**
 * packageName:crp.kr.api.auth.domains
 * fileName        :Role
 * author           : chohyungook
 * date               :2022-05-23
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-23 chohyungook 최초생성
 */
@Getter//읽기전용 (수정불가)
@RequiredArgsConstructor
public enum Role implements GrantedAuthority {
    ADMIN("ROLE_ADMIN","관리자권한"),
    USER("ROLE_USER","사용자권한"),
    UNKNOWN_USER("ROLE_UNKNOWN_USER","알수없는 사용자")
    ;
    private final String code;
    private final String description;

    public static Role of(String code) {
        return Arrays.stream(Role.values()).filter(i -> i.getCode().equals(code))
                .findAny().orElse(UNKNOWN_USER);//코드가 없을땐 언노운 유저로 나오게 해라.
    }

    @Override
    public String getAuthority() {
        return name();
    }
}
