from flask import Flask, render_template, request
import folium

taipai = Flask(__name__)

@taipai.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        act = request.form.get('act')
        location = request.form.get('location')
        if act == '上車' and location == '曼哈頓':
            return render_template('world_Manhattan.html')
        elif act == '上車' and location == '布魯克林區':
            return render_template('world_Brooklyn.html')
        elif act == '上車' and location == '皇后區(含機場)':
            return render_template('world_Queens.html')
        elif act == '上車' and location == '布朗克斯':
            return render_template('world_Bronx.html')
        elif act == '上車' and location == '史泰登島':
            return render_template('world_StatenIsland.html')
        elif act == '下車' and location == '曼哈頓':
            return render_template('world1_Manhattan.html')
        elif act == '下車':
            return render_template('world1.html')
        elif act == '下車' and location == '布魯克林區':
            return render_template('world1_Brooklyn.html')
        elif act == '下車' and location == '皇后區(含機場)':
            return render_template('world1Queens.html')
        elif act == '下車' and location == '布朗克斯':
            return render_template('world1_Bronx.html')
        elif act == '下車' and location == '史泰登島':
            return render_template('world1_Manhattan.html')
    
    return render_template('taipai.html')

if __name__ == '__main__':
    taipai.run(debug=True, port= 3000, host= '0.0.0.0')
