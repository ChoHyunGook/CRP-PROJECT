package crp.kr.api.auth.filter;

import crp.kr.api.auth.config.AuthProvider;
import crp.kr.api.auth.exception.SecurityRuntimeException;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.filter.OncePerRequestFilter;

import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

/**
 * packageName:crp.kr.api.auth.filter
 * fileName        :AuthFilter
 * author           : chohyungook
 * date               :2022-05-25
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-25chohyungook최초 생성
 */
@RequiredArgsConstructor
public class AuthFilter extends OncePerRequestFilter {
    private final AuthProvider provider;
    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
        String token = provider.resolveToken(request);
        try {
            if(token != null && provider.validateToken(token)){
                Authentication auth = provider.getAuthenticate(token);
                SecurityContextHolder.clearContext();
                SecurityContextHolder.getContext().setAuthentication(auth);
            }
        }
        catch (SecurityRuntimeException ex) {
            //this is very important, since it guarantees the user is not authenticated at all
            SecurityContextHolder.clearContext();
            response.sendError(ex.getHttpStatus().value(), ex.getMessage());
            return;
        } catch (Exception e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        filterChain.doFilter(request,response);
    }
}
