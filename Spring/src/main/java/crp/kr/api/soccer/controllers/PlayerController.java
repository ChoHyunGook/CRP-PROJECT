package crp.kr.api.soccer.controllers;

import crp.kr.api.soccer.domains.Player;
import crp.kr.api.soccer.services.PlayerService;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

/**
 * packageName:crp.kr.api.Soccer.controllers
 * fileName        :SoccerController
 * author           : chohyungook
 * date               :2022-05-09
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-09chohyungook최초 생성
 */
@RestController
@RequiredArgsConstructor
@RequestMapping("/player")
public class PlayerController {
    private final PlayerService service;

    @GetMapping("/findAll")
    public List<Player> findAll() {
        return service.findAll();
    }

    @GetMapping("/findAll/sort")
    public List<Player> findAll(Sort sort) {
        return service.findAll(sort);
    }

    @GetMapping("/findAll/pageable")
    public Page<Player> findAll(Pageable pageable) {
        return service.findAll(pageable);
    }

    @GetMapping("/count")
    public long count() {
        return service.count();
    }

    @DeleteMapping("/delete")
    public String delete(@RequestBody Player player) {
        return service.delete(player);
    }

    @PostMapping("/save")
    public String save(@RequestBody Player player) {
        return service.save(player);
    }

    @GetMapping("/findById/{playerNo}")
    public Optional<Player> findById(@PathVariable Long playerNo) { return service.findById(playerNo); }

    @GetMapping("/existsById/{playerNo}")
    public boolean existsById(@PathVariable Long playerNo) {  return service.existsById(playerNo); }
}
