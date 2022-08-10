package crp.kr.api.soccer.repositories;

import crp.kr.api.soccer.domains.Team;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * packageName:crp.kr.api.Soccer.repositories
 * fileName        :TeamRepository
 * author           : chohyungook
 * date               :2022-05-19
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-19chohyungook최초 생성
 */
interface TeamCustomRepository {
    //  000. 팀의 전화번호와 팩스번호를 수정하시오.
    @Query(value = "update Team t set t.tel = :tel, t.fax = :fax where t.teamNo = :teamNo", nativeQuery = true)
    int update(@Param("tel") String tel, @Param("fax") String fax, @Param("teamNo") Long teamNo);

    //  001. 전체 축구팀 목록을 팀이름 오름차순으로 출력하시오.
    @Query(value = "select t.teamName as teamName from Team t order by t.teamName asc ", nativeQuery = true)
    List<String> findTeamNamesAsc();

    //  002.
}

@Repository
public interface TeamRepository extends JpaRepository<Team, Long>, TeamCustomRepository {

}
