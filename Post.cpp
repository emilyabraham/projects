# include <iostream>
# include <string>
# include <stdexcept>
# include <sstream>
# include "Post.h"

using std::string, std::vector, std::ifstream, std::istringstream;

Post::Post(unsigned int postId, string userName, string postText) : postId(postId), userName(userName), postText(postText) {
    if (postId == 0 || userName == "" || postText == "") {
        throw std::invalid_argument("post constructor: invalid parameter values");
    }
}

unsigned int Post::getPostId() {
    return postId;
}

string Post::getPostUser() {
    return userName;
}

string Post::getPostText() {
    return postText;
}

vector<string> Post::findTags() {
    // TODO: extracts candidate tags based on occurrences of # in the post
    istringstream str1(postText); //string stream
    string str2; //stores word
    bool In = false; //check if word is already in the vector
  
    vector<string> tags;
    while(str1 >> str2){
        if(str2[0] != '#'){
        continue;
        }
    //all lowercase
        for(unsigned int i = 1; i < str2.length(); i++){ 
        str2[i] = tolower(str2[i]);
        }
    //takes off punctuation 
        while(str2[str2.length() - 1] == '!' || str2[str2.length() - 1] == '?' || str2[str2.length() - 1] == ',' || str2[str2.length() - 1] == '.'){
        str2.pop_back(); 
        }

        for(unsigned int i = 0; i < tags.size(); i++){
            if(tags[i] == str2){
            In = true;
            break;
        }
    }

        if(In == false){
            tags.push_back(str2);
        }

        In = false;
    }
    
    return tags;
}
