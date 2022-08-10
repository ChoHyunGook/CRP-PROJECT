package crp.kr.api.user.services;

import crp.kr.api.auth.domains.Messenger;
import crp.kr.api.user.domains.User;
import crp.kr.api.user.domains.UserDTO;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;

import java.util.List;
import java.util.Optional;

/**
 * packageName:crp.kr.api.services
 * fileName        :UserService
 * author           : chohyungook
 * date               :2022-05-03
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-03chohyungook최초 생성
 */
// Repository에 데이터를 넘겨줌 → 미들웨어
// 자바에서 미들웨어는 인터페이스로 만듦
public interface UserService {
    UserDTO login(UserDTO user); // 추상 메소드만 가짐 → Component 아님

    List<User> findAll();

    List<User> findAll(Sort sort);

    Page<User> findAll(Pageable pageable);

    Messenger count();

    Messenger update(User user);

    Messenger delete(User user);

    Messenger save(UserDTO user);

    Optional<User> findById(String userid);

    Messenger existsById(String userid);

    // custom
    List<User> findByUserName(String name);

    Messenger logout();
}
