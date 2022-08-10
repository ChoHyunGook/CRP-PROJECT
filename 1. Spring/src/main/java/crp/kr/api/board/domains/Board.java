package crp.kr.api.board.domains;

import com.sun.istack.NotNull;
import lombok.*;
import org.springframework.stereotype.Component;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

/**
 * packageName:crp.kr.api.domains
 * fileName        :Board
 * author           : chohyungook
 * date               :2022-05-04
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-04chohyungook최초 생성
 */
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Component
@Entity
@Table(name="boards")
public class Board {
    @Id
    @Column(name = "board_id")
    @GeneratedValue
    private long boardId;
    @Column private @NotNull
    String boardName; // Q&A ...
    @Column(name = "created_date") @NotNull private String createdDate;

    @OneToMany(mappedBy = "board")
    List<Article> articles = new ArrayList<>();
}