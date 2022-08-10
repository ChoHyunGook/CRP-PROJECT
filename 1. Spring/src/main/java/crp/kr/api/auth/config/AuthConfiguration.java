package crp.kr.api.auth.config;

import org.modelmapper.ModelMapper;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpMethod;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.builders.WebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;

/**
 * packageName:crp.kr.api.config
 * fileName        :WebSecurityConfig
 * author           : chohyungook
 * date               :2022-05-23
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-23chohyungook최초 생성
 */
@Configuration//filter기능 => 여기 통해서 restcontroller로 이동하게함
public class AuthConfiguration extends WebSecurityConfigurerAdapter {//외부 시크리티

        @Bean
        public PasswordEncoder passwordEncoder(){
            return new BCryptPasswordEncoder();
        }
        @Bean
        public ModelMapper modelMapper() {
            return new ModelMapper();
        }
        @Override
        public void configure(WebSecurity web) throws Exception {
            web.ignoring()
                    .antMatchers(HttpMethod.OPTIONS,"*/**")
                    .antMatchers("/");
        }
        @Override
        public void configure(HttpSecurity http) throws Exception {
            http.csrf().disable();
            http.sessionManagement().sessionCreationPolicy(SessionCreationPolicy.STATELESS);
            http.authorizeRequests()
                    .antMatchers("/users/join").permitAll()
                    .antMatchers("/users/login").permitAll()
                    .anyRequest().authenticated();
            http.exceptionHandling().accessDeniedPage("/users/login");
        }
    }

