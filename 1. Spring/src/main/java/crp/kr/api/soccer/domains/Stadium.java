package crp.kr.api.soccer.domains;

import lombok.*;
import org.springframework.stereotype.Component;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

/**
 * packageName:crp.kr.api.Soccer.domains
 * fileName        :Stadium
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
@Table(name = "stadiums")
public class Stadium {
    @Id
    @Column(name = "stadium_no")
    @GeneratedValue(strategy = GenerationType.IDENTITY) private Long stadiumNo;
    @Column(nullable = false) private String stadiumId;
    private String stadiumName;
    private String hometeamId;
    private String seatCount;
    private String address;
    private String ddd;
    private String tel;

    @OneToMany(mappedBy = "stadium")
    List<Schedule> schedules = new ArrayList<>();
}
