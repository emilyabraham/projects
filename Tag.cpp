# include <string>
# include <stdexcept>
# include "Tag.h"

using std::string, std::vector;

Tag::Tag(string tagName) :tagName(tagName) {
    // TODO: implement constructor checks
    //initial checks
    if(tagName.length() < 2 || tagName[0] != '#' || tagName[1] < 97 || tagName[1] > 122 || tagName[tagName.length() - 1] == '!' || tagName[tagName.length() - 1] == '?' || tagName[tagName.length() - 1] == ',' || tagName[tagName.length() - 1] == '.'){
        throw std::invalid_argument("invalid constructor ");
    }

    for(unsigned int i = 1; i < tagName.length(); i++){
        if(isupper(tagName[i])){ // if any of the letters are uppercase
        throw std::invalid_argument("invalid constructor ");
        }
    }
}

string Tag::getTagName() {
    // TODO: implement getter
    return tagName;
}

vector<Post*>& Tag::getTagPosts() {
    // TODO: implement getter
    return tagPosts;
}

void Tag::addTagPost(Post* post) {
    // TODO: add post to tag posts
    if(post == nullptr){
        throw std::invalid_argument("post is nullptr");
    }
    else{
        tagPosts.push_back(post);
    }
}
