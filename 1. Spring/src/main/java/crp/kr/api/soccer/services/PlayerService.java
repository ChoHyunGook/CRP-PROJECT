package crp.kr.api.soccer.services;

import crp.kr.api.soccer.domains.Player;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;

import java.util.List;
import java.util.Optional;

/**
 * packageName:crp.kr.api.Soccer.services
 * fileName        :PlayerService
 * author           : chohyungook
 * date               :2022-05-19
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-19chohyungook최초 생성
 */

public interface PlayerService {
    List<Player> findAll();

    List<Player> findAll(Sort sort);

    Page<Player> findAll(Pageable pageable);

    long count();

    String delete(Player player);

    String save(Player player);

    Optional<Player> findById(Long playerNo);

    boolean existsById(Long playerNo);
}
