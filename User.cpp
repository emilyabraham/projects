# include <string>
# include <stdexcept>
# include "User.h"

using std::string, std::vector;

User::User(string userName) : userName(userName){
    // TODO: implement constructor checks
    if(userName == "" || userName[0] < 97 || userName[0] > 122){ //for letters in ASCII
        throw std::invalid_argument("invalid constructor");
    }

    for(unsigned int i = 0; i < userName.length(); i++){
        if(isupper(userName[i])){
            throw std::invalid_argument("invalid constructor");
        }
    }

}

string User::getUserName() {
    // TODO: implement getter
    return userName;
}

vector<Post*>& User::getUserPosts() {
    // TODO: implement getter
    return userPosts;
}

void User::addUserPost(Post* post) {
    // TODO: add post to user posts
    if(post == nullptr){
        throw std::invalid_argument("post is nullptr!");
    }
    else{
        userPosts.push_back(post);
    }
}
