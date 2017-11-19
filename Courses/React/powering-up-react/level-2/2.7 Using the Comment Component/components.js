class CommentBox extends React.Component {
    render() {
      return(
        <div className="comment-box">
          <h3>Comments</h3>
          <h4 className="comment-count">2 comments</h4>
          <div className="comment-list">
            <Comment 
              author="Anne Droid" body="I want to know what love is..."/>
          </div>
        </div>
      );
    }
  }
  
  class Comment extends React.Component {
    render() {
      return(
        <div className="comment">
          <p className="comment-header">
            {this.props.author}
          </p>
          <p className="comment-body">
            {this.props.body}
          </p>
          <div className="comment-actions">
            <a href="#">Delete comment</a>
          </div>
        </div>
      );
    }
  }
  