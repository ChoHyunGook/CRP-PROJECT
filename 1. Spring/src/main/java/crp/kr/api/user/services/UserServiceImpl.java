package crp.kr.api.user.services;

import crp.kr.api.auth.config.AuthProvider;
import crp.kr.api.auth.domains.Messenger;
import crp.kr.api.auth.exception.SecurityRuntimeException;
import crp.kr.api.user.domains.Role;
import crp.kr.api.user.domains.User;
import crp.kr.api.user.domains.UserDTO;
import crp.kr.api.user.repositories.UserRepository;
import crp.kr.api.common.dataStructure.Box;
import lombok.RequiredArgsConstructor;
import org.modelmapper.ModelMapper;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.http.HttpStatus;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import static crp.kr.api.common.lambdas.Lambda.*;

/**
 * packageName:crp.kr.api.services
 * fileName        :UserServiceImpl
 * author           : chohyungook
 * date               :2022-05-03
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-03chohyungook최초 생성
 */
@Service
@RequiredArgsConstructor
public class UserServiceImpl implements UserService {
    private final UserRepository repository;
    private final PasswordEncoder encoder;
    private final AuthProvider provider;
    private final ModelMapper modelMapper;

    @Override
    public UserDTO login(UserDTO paramUser) {
        try{
            UserDTO returnUser = new UserDTO();
            String username = paramUser.getUsername();
            User findUser = repository.findByUsername(username).orElse(null);
            if(findUser != null){
                boolean checkPassword = encoder.matches(paramUser.getPassword(), findUser.getPassword());
                if(checkPassword){
                    returnUser = modelMapper.map(findUser, UserDTO.class);
                    String token = provider.createToken(username, returnUser.getRoles());
                    returnUser.setToken(token);
                }else{
                    String token = "FAILURE";
                    returnUser.setToken(token);
                }
            }
            return returnUser;
        }catch (Exception e){
            throw new SecurityRuntimeException("유효하지 않은 아이디/비밀번호", HttpStatus.UNPROCESSABLE_ENTITY);
        }
    }

    @Override
    public List<User> findAll() {
        return repository.findAll();
    }

    @Override
    public List<User> findAll(Sort sort) {
        return repository.findAll();
    }

    @Override
    public Page<User> findAll(Pageable pageable) {
        return repository.findAll(pageable);
    }

    @Override
    public Messenger count() {
        return Messenger.builder().message(string(repository.count())).build();
    }

    @Override
    public Messenger update(User user) {
        return Messenger.builder().build();
    }

    @Override
    public Messenger delete(User user) {
        repository.delete(user);
        return Messenger.builder().message("").build();
    }

    @Override
    public Messenger save(UserDTO user) {
        System.out.println("서비스로 전달된 회원가입 정보 : " + user.toString());
        String result = "";
        if(repository.findByUsername(user.getUsername()).isEmpty()){
            List<Role> list = new ArrayList<>();
            list.add(Role.USER);
            repository.save(User.builder()
                    .username(user.getUsername())
                    .name(user.getName())
                    .regDate(user.getRegDate())
                    .email(user.getEmail())
                    .password(encoder.encode(user.getPassword()))
                    .roles(list).build());
            result = "SUCCESS";
        }else{
            result = "FAIL";
        }
        return Messenger.builder().message(result).build();
    }

    @Override
    public Optional<User> findById(String userid) {
        return repository.findById(0L); // userid 타입이 다름
    }

    @Override
    public Messenger existsById(String userid) {
        return repository.existsById(longParse(userid))
                ? Messenger.builder().message("EXIST").build()
                : Messenger.builder().message("NOT_EXIST").build(); // userid 타입이 다름
    }

    @Override
    public List<User> findByUserName(String name) {
        List<User> ls = repository.findAll();
        Box<String, User> box = new Box<>();
        // ls = box.findByUserName(ls, name);
        // ls.stream().filter(...)
        return null;
    }

    @Override
    public Messenger logout() {
        return Messenger.builder().build();
    }
}
