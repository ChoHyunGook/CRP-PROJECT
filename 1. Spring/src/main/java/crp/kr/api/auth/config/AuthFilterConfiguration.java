package crp.kr.api.auth.config;

import lombok.RequiredArgsConstructor;
import org.springframework.security.config.annotation.SecurityConfigurerAdapter;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.web.DefaultSecurityFilterChain;

/**
 * packageName:crp.kr.api.config
 * fileName        :SecurityConfig
 * author           : chohyungook
 * date               :2022-05-23
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-23chohyungook최초 생성
 */
@RequiredArgsConstructor
public class AuthFilterConfiguration extends SecurityConfigurerAdapter<DefaultSecurityFilterChain, HttpSecurity> {//내부시크리티

    @Override
    public void configure(HttpSecurity builder) throws Exception {
        super.configure(builder);
    }
}
