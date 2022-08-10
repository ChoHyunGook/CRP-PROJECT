package crp.kr.api.user.controllers;

import crp.kr.api.auth.domains.Messenger;
import crp.kr.api.user.domains.User;
import crp.kr.api.user.domains.UserDTO;
import crp.kr.api.user.services.UserService;
import io.swagger.annotations.*;
import lombok.RequiredArgsConstructor;
import org.modelmapper.ModelMapper;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

/**
 * packageName:crp.kr.api.controllers
 * fileName        :UserController
 * author           : chohyungook
 * date               :2022-05-03
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-03chohyungook최초 생성
 */
@CrossOrigin(origins = "*", allowedHeaders = "*")
@Api(tags = "users")
@RestController // @Component의 자식
@RequiredArgsConstructor // 필수 파라미터 → 리액트에서 props → 자식
@RequestMapping("/users")
public class UserController {
    /*
    private UserService service;
    public UserController(UserService service){
        service = new UserServiceImpl();
    }
    */
    private final UserService service; // 자동으로 controller의 생성자 안에 service가 들어감 → controller가 자식, service가 부모
    private final ModelMapper modelMapper;//대응시키는거 map=>1:1,reducer=>다대일,filter=>1:?


    @ApiOperation(value = "${UserController.login}")
    @PostMapping("/login")
    @ApiResponses(value={
            @ApiResponse(code=400,message = "Something Wrong"),
            @ApiResponse(code=422, message = "유효하지 않은 아이디/비밀번호")
    })
    public ResponseEntity<UserDTO> login(@ApiParam("Login User") @RequestBody UserDTO user) {
        return ResponseEntity.ok(service.login(user));
    }

    @GetMapping("/logout")
    public ResponseEntity<Messenger> logout(@RequestBody User user) {
        return ResponseEntity.ok(service.logout());
    }

    @GetMapping("/findAll")
    public ResponseEntity<List<User>> findAll() {
        return ResponseEntity.ok(service.findAll());
    }

    @GetMapping("/findAll/sort")
    public ResponseEntity<List<User>> findAll(Sort sort) {
        return ResponseEntity.ok(service.findAll(sort));
    }

    @GetMapping("/findAll/pageable")
    public ResponseEntity<Page<User>> findAll(Pageable pageable) {
        return ResponseEntity.ok(service.findAll(pageable));
    }

    @GetMapping("/count")
    public ResponseEntity<Messenger> count() {
        return ResponseEntity.ok(service.count());
    }

    @PutMapping("/update")
    public ResponseEntity<Messenger> update(@RequestBody User user) {
        service.update(user);
        return ResponseEntity.ok(service.update(user));
    }

    @DeleteMapping("/delete")
    public ResponseEntity<Messenger> delete(@RequestBody User user) { // 관리자
        service.delete(user);
        return ResponseEntity.ok(service.delete(user));
    }
    @ApiOperation(value = "${UserController.join}")
    @PostMapping("/join")
    @ApiResponses(value={
            @ApiResponse(code=400,message = "Something Wrong"),
            @ApiResponse(code=403,message = "승인거절"),
            @ApiResponse(code=422, message = "중복된ID")
    })
    public ResponseEntity<Messenger> save(@ApiParam("Join User") @RequestBody UserDTO user) {
        System.out.println("회원가입정보 : "+ user.toString());//나중에 꼭지워라!
        return ResponseEntity.ok(service.save(user));
    }

    @GetMapping("/findById/{userid}")
    public ResponseEntity<Optional<User>> findById(@PathVariable String userid) { // path = url → {userid}
        return ResponseEntity.ok(service.findById(userid));
    }

    @GetMapping("/existsById/{userid}")
    public ResponseEntity<Messenger> existsById(@PathVariable String userid) {
        return ResponseEntity.ok(service.existsById(userid));
    }


}
