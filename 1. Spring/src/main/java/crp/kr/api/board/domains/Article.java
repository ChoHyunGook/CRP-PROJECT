package crp.kr.api.board.domains;

import com.sun.istack.NotNull;
import crp.kr.api.user.domains.User;
import lombok.*;
import org.springframework.data.repository.cdi.Eager;
import org.springframework.stereotype.Component;

import javax.persistence.*;


/**
 * packageName:crp.kr.api.board.domains
 * fileName        :Article
 * author           : chohyungook
 * date               :2022-05-09
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-09chohyungook최초 생성
 */
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Component
@Entity
@Eager // 즉시 실행 → 테이블은 실행하자마자 즉시 만들어져야 함 (↔ @Lazy)
@Table(name = "articles")
public class Article { // 게시글, article이 있는 곳이 board
    @Id
    @Column(name = "article_id")
    @GeneratedValue private long articleId;
    @Column @NotNull private String title;
    @Column @NotNull private String content;
    @Column(name = "written_date") @NotNull private String writtenDate; // 여기까지 빌더

    // 관계
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "user_id") // 외래키 매핑
    private User user; // article의 입장에서 누가 주인인지 모르기 때문에 객체 생성 X -> Lazy (객체 생성 시점 조절)

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "board_id")
    private Board board;
}