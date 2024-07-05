
export class NumberKind{
    id='';
    name='';
    description='';
    min_len=''
    url_end_point='';
    is_serie='';

    constructor (id, name, description, min_len, end_point, is_serie){
        this.id=id;
        this.name=name;
        this.description=description;
        this.min_len=min_len;
        this.url_end_point=end_point;
        this.is_serie=is_serie;
    }
}
