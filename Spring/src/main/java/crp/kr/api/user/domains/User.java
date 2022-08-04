package crp.kr.api.user.domains;

import com.sun.istack.NotNull;
import crp.kr.api.board.domains.Article;
import lombok.*;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;


/**
 * packageName:crp.kr.api.domains
 * fileName        :User
 * author           : chohyungook
 * date               :2022-05-03
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-03chohyungook최초 생성
 */
@Builder
@Getter
@NoArgsConstructor
@AllArgsConstructor
@ToString
@Setter
// 컴포넌트는 property와 method의 집합이다.
// 리액트에서 컴포넌트는 props와 state, 그리고 render()를 가진 순수 함수이다.
@Entity
@Table(name = "users")
public class User {
        @Id
        @Column(name = "user_id")
        @GeneratedValue private long userId;
        @Column private @NotNull String username;
        @Column private @NotNull String password;
        @Column private @NotNull String name;
        @Column private @NotNull String email;
        @Column(name = "reg_date") @NotNull private String regDate;

        //    TIP : 외래 키가 있는 곳을 연관 관계의 주인으로 정하면 됩니다. 무조건.
        @OneToMany(mappedBy = "user") // user가 있어야 매핑됨 (Lazy 보장)
                // 연관관계의 주인을 지정 // 데이터베이스 입장에서는 무조건 다(N) 쪽에서 외래키를 관리 // 테이블은 무조건 양방향
                List<Article> articles = new ArrayList<>(); // user가 쓴 글들을 모아놓는 공간 → 객체 생성 -> Eager

        @ElementCollection(fetch = FetchType.EAGER)
        public List<Role> roles;
}
