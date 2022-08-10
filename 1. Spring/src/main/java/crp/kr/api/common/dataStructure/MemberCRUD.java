package crp.kr.api.common.dataStructure;


import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.RequiredArgsConstructor;

import java.util.*;
import java.util.stream.Collectors;

/**
 * packageName:crp.kr.api.common.dataStructure
 * fileName        :MemberCRUD
 * author           : chohyungook
 * date               :2022-05-09
 * desc            :
 * ================================
 * DATE              AUTHOR        NOTE
 * ================================
 * 2022-05-09chohyungook최초 생성
 */
public class MemberCRUD {
    @Data
    @NoArgsConstructor
    static class Member { // domain
        protected String userid, name, password, profileImg, phone, email;

        public Member (Builder builder) { // builder는 모든 정보를 다 갖고 있음
            this.userid = builder.userid;
            this.name = builder.name;
            this.password = builder.password;
            this.profileImg = builder.profileImg;
            this.phone = builder.phone;
            this.email = builder.email;
        }

        static class Builder {
            private String userid, name, password, profileImg, phone, email;
            public Builder (String userid) { this.userid = userid; }
            public Builder name(String name) { this.name = name; return this; }
            public Builder password(String password) { this.password = userid; return this; }
            public Builder profileImg(String profileImg) { this.profileImg = profileImg; return this; }
            public Builder phone(String phone) { this.phone = phone; return this; }
            public Builder email(String email) { this.email = email; return this; }
            Member build() { return new Member(this); }
        }

        @Override
        public String toString() {
            return String.format("[사용자 스펙] userid : %s, name : %s, password : %s, profileImg : %s, phone : %s, email : %s",
                    userid, name, password, profileImg, phone, email);
        }
    }

    public static void main(String[] args) { // controller
        Scanner s = new Scanner(System.in);
        MemberService service = new MemberServiceImpl();
        while (true) {
            System.out.println("0.exit 1.save 2.update 3.delete 4.findById 5.findByName 6.findAll 7.count 8.existsById");
            switch (s.next()) {
                case "0" : return;
                case "1" :
                    Member hong = new Member.Builder("hong") // 대문자는 전부 static
                            .email("hong@test.com")
                            .password("1")
                            .name("홍길동")
                            .phone("010-0000-9999")
                            .profileImg("hong.jpg")
                            .build();
                    service.save(hong);
                    Member kim = new Member.Builder("kim")
                            .email("kim@test.com")
                            .password("1")
                            .name("김유신")
                            .phone("010-0044-9944")
                            .profileImg("kim.jpg")
                            .build();
                    service.save(kim);
                    Member you = new Member.Builder("you")
                            .email("you@test.com")
                            .password("1")
                            .name("유관순")
                            .phone("010-0880-9889")
                            .profileImg("you.jpg")
                            .build();
                    service.save(you);
                    break;
                case "2" :
                    kim = new Member.Builder("kim")
                            .email("kim@test.com")
                            .password("1")
                            .name("김유신")
                            .phone("010-1111-2222")
                            .profileImg("kim.jpg")
                            .build();
                    service.update(kim);
                    System.out.println(kim.name + "의 전화번호 update 완료 : " + kim.phone);
                    break;
                case "3" :
                    Member temp = new Member();
                    temp.setUserid("kim");
                    if (service.existsById("kim")){
                        service.delete(temp);
                        System.out.println("유저 삭제가 완료됐습니다.");
                    }
                    else {
                        System.out.println("해당 유저가 없습니다.");
                    }

                    break;
                case "4" :
                    String res = service.existsById("kim")? service.findById("kim").toString() : "해당 유저가 없습니다.";
                    System.out.println(res);
                    break;
                case "5" :
                    System.out.println(service.findByName("홍길동"));
                    break;
                case "6" :
                    System.out.println("총 회원목록 : " + service.findAll());
                    break;
                case "7" :
                    System.out.println(service.count());
                    break;
                case "8" :
                    System.out.println(service.existsById("hong"));
                    break;
                default : break;
            }
        }
    }

    interface MemberService{ // service
        void save(Member member);
        void update(Member member);
        void delete(Member member); // CUD는 consumer
        Member findById(String id);
        List<Member> findByName(String name);
        List<Member> findAll();
        int count();
        boolean existsById(String id);
    }

    //    @RequiredArgsConstructor // MemberServiceImpl(Map<String, Member> map){}
    static class MemberServiceImpl implements MemberService{
        private final Map<String, Member> map; // 메모리에 존재하는 DB 역할 (리덕스의 store) // props
        private final List<Member> list;
        public MemberServiceImpl() {
            map = new HashMap<>();
            this.list = new ArrayList<>();
        }
        @Override
        public void save(Member member){ map.put(member.getUserid(), member); }

        @Override
        public void update(Member member) {
            map.replace(member.getUserid(), member);
        }

        @Override
        public void delete(Member member) {
            map.remove(member.getUserid());
        }

        @Override
        public Member findById(String id) {
            return map.get(id);
        }

        @Override
        public List<Member> findByName(String name) {
            List<Member> members = new ArrayList<Member>();
            map.forEach((key, value) -> {
                if (value.name.equals(name)) {
                    members.add(value);
                }
            });
            return members;
        }

        @Override
        public List<Member> findAll() {
            return map.values().stream().collect(Collectors.toList());
        }

        @Override
        public int count() {
            return map.size();
        }

        @Override
        public boolean existsById(String id) {
            return map.containsKey(id);
        }

    }
}
